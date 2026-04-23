"""
Pocket Option WebSocket Test for Railway - CORRECTED
"""

import asyncio
from pocketoptionapi_async import AsyncPocketOptionClient

# Your SSID
SSID = '42["auth",{"session":"90dcda6b139fe52217664e80d6930ace","isDemo":1,"uid":88209425,"platform":2,"isFastHistory":true,"isOptimized":true}]'

async def test():
    print("=" * 60)
    print("Pocket Option WebSocket Test on Railway")
    print("=" * 60)
    
    try:
        print("\n[1] Creating client...")
        client = AsyncPocketOptionClient(ssid=SSID)
        print("   ✅ Client created")
        
        print("\n[2] Connecting to Pocket Option...")
        await client.connect()
        print("   ✅ Connected!")
        
        print("\n[3] Testing candle fetch...")
        
        # Try different method signatures
        # Method 1: positional arguments (asset, timeframe, count)
        try:
            candles = await client.get_candles("EURUSD_otc", 60, 10)
            print(f"   ✅ Got {len(candles)} candles (positional args)")
            print(f"   Latest candle: {candles[-1] if candles else 'None'}")
        except TypeError as e:
            print(f"   ⚠️ Positional args failed: {e}")
            
            # Method 2: try with different parameter names
            try:
                candles = await client.get_candles(asset="EURUSD_otc", size=10, timeframe=60)
                print(f"   ✅ Got {len(candles)} candles (asset, size, timeframe)")
            except TypeError as e2:
                print(f"   ⚠️ Named args failed: {e2}")
                
                # Method 3: try the sync version
                try:
                    from pocketoptionapi_async import PocketOptionClient
                    sync_client = PocketOptionClient(ssid=SSID)
                    sync_client.connect()
                    candles = sync_client.get_candles("EURUSD_otc", 60, 10)
                    print(f"   ✅ Got {len(candles)} candles (sync client)")
                    await sync_client.disconnect()
                except Exception as e3:
                    print(f"   ❌ All methods failed: {e3}")
        
        print("\n[4] Keeping connection alive for 30 seconds...")
        for i in range(6):
            await asyncio.sleep(5)
            print(f"   Still connected... {i+1}/6")
        
        print("\n[5] Disconnecting...")
        await client.disconnect()
        print("   ✅ Disconnected")
        
        print("\n" + "=" * 60)
        print("🎉 Test complete!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
