from psycopg.rows import dict_row

from app.database.connection import get_connection


async def get_weekly_stats() -> list[dict]:
    """Return per-user link counts for the last 7 days, ordered by total desc."""
    async with await get_connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                """
                SELECT
                    user_id,
                    username,
                    COUNT(*) AS total,
                    COUNT(*) FILTER (WHERE link_type = 'tiktok')          AS tiktok,
                    COUNT(*) FILTER (WHERE link_type = 'youtube_shorts')  AS youtube,
                    COUNT(*) FILTER (WHERE link_type = 'instagram')       AS instagram
                FROM link_stats
                WHERE sent_at >= NOW() - INTERVAL '7 days'
                GROUP BY user_id, username
                ORDER BY total DESC
                LIMIT 10
                """
            )
            return await cur.fetchall()


def format_leaderboard(rows: list[dict]) -> str:
    if not rows:
        return "No link spam this week. Miracles do happen."

    medals = ["🥇", "🥈", "🥉"]
    lines = ["*Weekly Link Spammer Leaderboard*", "_Last 7 days_", ""]

    for i, row in enumerate(rows):
        medal = medals[i] if i < 3 else f"{i + 1}."
        name = f"@{row['username']}" if row["username"] else f"user {row['user_id']}"
        lines.append(f"{medal} {name} — *{row['total']}* links")

    total_tiktok = sum(r["tiktok"] for r in rows)
    total_youtube = sum(r["youtube"] for r in rows)
    total_instagram = sum(r["instagram"] for r in rows)

    lines += [
        "",
        f"TikTok: {total_tiktok}  |  YT Shorts: {total_youtube}  |  Instagram: {total_instagram}",
    ]

    return "\n".join(lines)
