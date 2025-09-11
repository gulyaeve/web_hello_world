from faststream.rabbit import RabbitQueue
from web.settings import broker


async def publish_image_to_queue(data: dict):
    img_queue = RabbitQueue("image_queue", auto_delete=True)

    await broker.connect()

    await broker.declare_queue(img_queue)

    await broker.publish(
        str(data),
        queue=img_queue
        )
    
    await broker.stop()
    