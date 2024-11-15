from typing import Dict

from fastapi import BackgroundTasks, FastAPI, HTTPException


app = FastAPI()


async def temp1():
    print("-------------temp1---------------")


async def temp2():
    print("-------------temp2---------------")


async def temp3():
    print("-------------temp3---------------")


async def temp4():
    print("-------------temp4---------------")


@app.get("/")
async def root(
    background_tasks: BackgroundTasks,
    first_name: str | None = "",
    last_name: str | None = "",
) -> Dict[str, str]:
    await temp2()
    await temp3()
    await temp4()
    background_tasks.add_task(temp1)
    return {"message": "Hello World"}


@app.put("/")
async def new(
    background_tasks: BackgroundTasks,
    first_name: str | None = "",
    last_name: str | None = "",
) -> Dict[str, str]:
    await temp2()
    await temp3()
    await temp4()
    background_tasks.add_task(temp1)
    return {"message": "Hello World - PUT"}


@app.get("/error")
async def error(raise_error: bool = False) -> Dict:
    if raise_error:
        raise HTTPException(status_code=400, detail="not found.")
    return {"message": "The error page!"}
