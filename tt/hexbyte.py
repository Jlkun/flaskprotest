# -*- coding: utf-8

def HexToByte( hexStr ):
    return bytes.fromhex(hexStr)

hexStr='33F9F14634A72A7C03D2707227749FC9D49D6332CE8156C1E5EA07830A569D646889294FACC3775344FF219A1361FBF853F93702BC9AC562BD93B903446073CECDB9BDE8B43D0DF5B238C8893781949D9F0A60EFAE4CB4119379D17FF6294FB978777580004442B748993C13655BD8666F4B0A88C384FC0E22D742ACC88A9A69'
print(HexToByte(hexStr))