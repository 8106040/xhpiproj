from azure.storage import BlobService

bs=BlobService(account_name='xhpi',account_key='LdfaFhlJpL8xJE3iFhgExDU8VRmA6s5M7b2s0Ztd2CrxX+6MVsFTHilHOJ3TuUCffluyaOgP7jYj8Na5J8g3+A==')

bs.put_block_blob_from_path('xhpicloud','pic.jpg','/home/pi/blobfile/pic.jpg')

bs.put_block_blob_from_path('xhpicloud','picpu.txt','/home/pi/blobfile/picpu.txt')

bs.put_block_blob_from_path('xhpicloud','envtemp.txt','/home/pi/blobfile/envtemp.txt')