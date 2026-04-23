"""
Eagle Lenz - Quotex Connection Test (2FA Disabled)
"""

import asyncio
import os
from pyquotex.stable_api import Quotex

# Get credentials from environment variables
QUOTEX_EMAIL = os.environ.get("QUOTEX_EMAIL", "your_email@example.com")
QUOTEX_PASSWORD = os.environ.get("QUOTEX_PASSWORD", "your_password")

async def test_quotex():
    print("=" * 60)
    print("Eagle Lenz - Quotex Connection Test (2FA OFF)")
    print("=" * 60)
    
    print("\n[1] Creating Quotex client...")
    client = Quotex(email=QUOTEX_EMAIL, password=QUOTEX_PASSWORD, lang="en")
    print("   ✅ Client created")
    
    print("\n[2] Connecting to Quotex...")
    try:
        check, message = await client.connect()
        
        if check:
            print("   ✅ Connected to Quotex!")
            
            print("\n[3] Getting account balance...")
            try:
                balance = client.get_balance()
                print(f"   ✅ Balance: ${balance}")
            except Exception as e:
                print(f"   ⚠️ Could not get balance: {e}")
            
            print("\n[4] Getting all assets...")
            assets = client.get_all_asset_name()
            print(f"   ✅ Found {len(assets)} assets")
            print(f"   First 10 assets: {assets[:10]}")
            
            print("\n[5] Testing candle fetch...")
            if assets:
                test_asset = assets[0]
                candles = client.get_candles(test_asset, period=60, count=10)
                print(f"   ✅ Got {len(candles)} candles for {test_asset}")
                if candles:
                    print(f"   Latest candle: {candles[-1]}")
            
            print("\n[6] Disconnecting...")
            await client.close()
            print("   ✅ Disconnected")
            
            print("\n" + "=" * 60)
            print("🎉 QUOTEX IS WORKING ON RAILWAY!")
            print("=" * 60)
            return True
            
        else:
            print(f"   ❌ Connection failed: {message}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_quotex())
