# # ----------------------------------- 사용하기 ----------------------------------- #

# # https://dojang.io/mod/page/view.php?id=2469
# import asyncio

# async def hello():    # async def로 네이티브 코루틴을 만듦
#     print('Hello, world!')

# loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
# loop.run_until_complete(hello())    # hello가 끝날 때까지 기다림
# loop.close()



# -------------------------------- 네이티브 코루틴 생성 ------------------------------- 성
# import asyncio

# async def add(a, b):
#     print('add: {0} + {1}'.format(a, b))
#     await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
#     return a + b    # 두 수를 더한 결과 반환

# async def print_add(a, b):
#     result = await add(a, b)    # await로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장
#     print('print_add: {0} + {1} = {2}'.format(a, b, result))

# loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
# loop.run_until_complete(print_add(1, 2))    # print_add가 끝날 때까지 이벤트 루프를 실행
# loop.close()                                # 이벤트 루프를 닫음

# """
# 퓨처(asyncio.Future)는 미래에 할 일을 표현하는 클래스인데 할 일을 취소하거나 상태 확인, 완료 및 결과 설정에 사용합니다.
# 태스크(asyncio.Task)는 asyncio.Future의 파생 클래스이며 asyncio.Future의 기능과 실행할 코루틴의 객체를 포함하고 있습니다.
#     태스크는 코루틴의 실행을 취소하거나 상태 확인, 완료 및 결과 설정에 사용합니다. 이 부분은 내용이 다소 복잡하므로 이정도까지만
#     설명하겠습니다.
# """

# ------------------------------- gather 사용해 보기 ------------------------------ #
import asyncio
import functools
ret = None
async def wait_sum(a,b,sec):
    await asyncio.sleep(sec)

    return(a+b)

async def main():
    #task = asyncio.create_task(wait_sum(1,2,3),name="task1")
    tasks = [asyncio.create_task(wait_sum(1,2,3),name="task1"),
            asyncio.create_task(wait_sum(3,4,5),name="task2")]
    result = await asyncio.gather(*tasks)
    print(result)

loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
loop.run_until_complete(main())    # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close()

