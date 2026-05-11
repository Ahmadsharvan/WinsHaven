#!/usr/bin/env python3
"""
Upgrade tickets from 500 to 1000
"""

import json
import os

TICKETS_FILE = "data/tickets.json"
TOTAL_TICKETS = 1000

def upgrade_tickets():
    """Upgrade tickets from 500 to 1000"""
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, 'r') as f:
            existing_tickets = json.load(f)
        
        max_existing = max(int(key) for key in existing_tickets.keys()) if existing_tickets else 0
        
        if max_existing < TOTAL_TICKETS:
            print(f"🔄 Upgrading tickets from {max_existing} to {TOTAL_TICKETS}")
            for i in range(max_existing + 1, TOTAL_TICKETS + 1):
                ticket_key = f"{i:04d}"
                existing_tickets[ticket_key] = {"available": True}
            
            with open(TICKETS_FILE, 'w') as f:
                json.dump(existing_tickets, f, indent=2)
            
            print(f"✅ Added {TOTAL_TICKETS - max_existing} new tickets")
            print(f"📊 Total tickets now: {len(existing_tickets)}")
        else:
            print(f"✅ Tickets already up to date with {max_existing} tickets")
    else:
        print("❌ Tickets file not found")

if __name__ == "__main__":
    upgrade_tickets()
