import orm,asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', database='myblog')
    u = User(name='Test', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destory_pool()


# async def test(loop):
#     await orm.create_pool(loop=loop, user='root', password='123456', database='myblog')
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#     await u.save()
#     await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

#for x in test():
#    pass