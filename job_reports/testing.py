import asyncio
import aiohttp

async def task1_cpu() -> None:
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task2_gpu() -> None:
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

# Run both tasks together
async def group_tasks():
    await asyncio.gather(task1_cpu(), task2_gpu())

if __name__ == "__main__":
    print(group_tasks())

