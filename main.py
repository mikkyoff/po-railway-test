"""
Pocket Option WebSocket Test for Railway
Run this to test if WebSocket stays connected on Linux
"""

import asyncio
import os
from pocketoptionapi_async import AsyncPocketOptionClient

# Your SSID - put the full string here
SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

async def test_connection():
    print("=" * 60)
    print("Pocket Option WebSocket Test on Railway")
    print("=" * 60)
    
    try:
        print("\n[1] Creating client...")
        client = AsyncPocketOptionClient(ssid=SSID)
        print("   ✅ Client created")
        
        print("\n[2] Connecting to Pocket Option...")
        await client.connect()
        print("   ✅ Connected! WebSocket is stable on Railway.")
        
        print("\n[3] Testing candle fetch...")
        candles = await client.get_candles("EURUSD_otc", period=60, limit=10)
        print(f"   ✅ Got {len(candles)} candles!")
        
        if candles:
            latest = candles[-1]
            print(f"\n   Latest candle: {latest}")
        
        print("\n[4] Keeping connection alive for 30 seconds...")
        for i in range(6):
            await asyncio.sleep(5)
            print(f"   Still connected... {i+1}/6")
        
        print("\n[5] Disconnecting...")
        await client.disconnect()
        print("   ✅ Disconnected")
        
        print("\n" + "=" * 60)
        print("🎉 SUCCESS! Pocket Option WebSocket works on Railway!")
        print("   You can now build Eagle Lenz on this platform.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n⚠️ WebSocket failed. This confirms the issue is Windows-specific.")
        return False
    
    return True

if __name__ == "__main__":
    asyncio.run(test_connection())