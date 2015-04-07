from azure.storage import BlobService

bs=BlobService(account_name='xhpi',account_key='LdfaFhlJpL8xJE3iFhgExDU8VRmA6s5M7b2s0Ztd2CrxX+6MVsFTHilHOJ3TuUCffluyaOgP7jYj8Na5J8g3+A==')

bs.put_block_blob_from_path('xhpicloud','pic.jpg','/home/pi/1.jpg')