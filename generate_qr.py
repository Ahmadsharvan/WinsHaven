#!/usr/bin/env python3
"""
UPI QR Code Generator for Lucky Draw Application
Generates real UPI QR codes that can be scanned by any UPI app
"""

import qrcode
import os
from datetime import datetime

def generate_upi_qr(upi_id, amount, name, note="Lucky Draw Tickets"):
    """
    Generate UPI QR code
    
    Args:
        upi_id (str): UPI ID (e.g., yourname@bank)
        amount (float): Amount to pay
        name (str): Payee name
        note (str): Payment note
    
    Returns:
        str: Path to generated QR code image
    """
    
    # Create UPI URL
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"
    
    print(f"Generated UPI URL: {upi_url}")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure static/images directory exists
    os.makedirs('static/images', exist_ok=True)
    
    # Save QR code
    filename = f"static/images/upi_qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    qr_image.save(filename)
    
    print(f"QR Code saved as: {filename}")
    return filename

def generate_static_qr():
    """Generate a static QR code for the main UPI ID"""
    
    # Static UPI ID for the application
    upi_id = "your-upi-id@bank"  # Replace with your actual UPI ID
    
    # Create a generic QR code that can be used for any amount
    upi_url = f"upi://pay?pa={upi_id}&pn=Lucky%20Draw&tn=Ticket%20Payment&cu=INR"
    
    print(f"Static UPI URL: {upi_url}")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure static/images directory exists
    os.makedirs('static/images', exist_ok=True)
    
    # Save as static UPI QR code
    filename = "static/images/upi_qr_static.png"
    qr_image.save(filename)
    
    print(f"Static QR Code saved as: {filename}")
    return filename

if __name__ == "__main__":
    print("🎯 UPI QR Code Generator for Lucky Draw")
    print("=" * 50)
    
    # Generate static QR code
    static_qr = generate_static_qr()
    
    # Generate sample QR codes for testing
    print("\n📱 Generating sample QR codes for testing...")
    
    # Sample 1: 1 ticket = ₹5
    generate_upi_qr("your-upi-id@bank", 5, "Test User", "1 Ticket")
    
    # Sample 2: 5 tickets = ₹25
    generate_upi_qr("your-upi-id@bank", 25, "Test User", "5 Tickets")
    
    # Sample 3: 10 tickets = ₹50
    generate_upi_qr("your-upi-id@bank", 50, "Test User", "10 Tickets")
    
    print("\n✅ QR codes generated successfully!")
    print(f"📁 Static QR code: {static_qr}")
    print("\n💡 Use the static QR code in your application")
    print("💡 Dynamic QR codes can be generated for specific amounts")
