# 🎯 Lucky Draw - Manual Payment System Guide

## 🔹 **What You've Got Now**

✅ **Manual payment verification system** with UPI integration  
✅ **WebSocket support** for real-time status updates  
✅ **Manual booking completion** when payment is verified  
✅ **Darker background** on all pages  
✅ **Professional payment interface** with status tracking

## 🔹 **How It Works (Manual Payment Flow)**

1. **User selects tickets** → **Clicks "Proceed to Payment"**
2. **Payment page shows** → **User sees UPI details and QR code**
3. **User completes UPI payment** → **Enters transaction ID**
4. **Admin verifies payment** → **Booking completed manually**
5. **Success page shown** → **Data saved to Excel**
6. **Tickets marked as booked** → **Process complete**

## 🔹 **What You Need to Do**

### **Step 1: Configure UPI Details**

1. **Open**: `lucky_draw/app_realtime.py`
2. **Replace the UPI ID**:
   ```python
   UPI_ID = "your-upi-id@bank"  # Replace with your actual UPI ID
   ```

### **Step 2: Set Up Payment Verification**

1. **Configure your UPI app** to receive payments
2. **Set up QR code** for easy payment scanning
3. **Train admin users** on payment verification process

### **Step 4: Run the Application**

```bash
# Install dependencies
pip install -r requirements.txt

# Run the real-time payment system
python app_realtime.py
```

## 🔹 **Files Created/Modified**

### **New Files:**

- `app_realtime.py` - Main application with real-time payments
- `templates/payment_realtime.html` - Real-time payment page
- `setup_realtime_payment.bat` - Setup script
- `requirements.txt` - Updated with new dependencies

### **Modified Files:**

- All template files - **Darker background** applied
- `requirements.txt` - Added WebSocket and Razorpay packages

## 🔹 **Features Included**

### **Manual Payment Features:**

- ✅ **UPI payment integration** with QR code support
- ✅ **Live payment status** updates via WebSockets
- ✅ **Manual booking completion** with admin verification
- ✅ **Transaction ID verification** system
- ✅ **Real-time status tracking** for payments
- ✅ **Admin dashboard** for payment management

### **UI/UX Features:**

- ✅ **Darker, warmer background** on all pages
- ✅ **Animated payment status** indicators
- ✅ **Real-time status messages**
- ✅ **Professional payment interface**
- ✅ **Mobile-responsive design**

### **Admin Features:**

- ✅ **Complete admin dashboard**
- ✅ **Real-time payment monitoring**
- ✅ **Data export and reset**
- ✅ **Booking management**

## 🔹 **Testing the System**

### **Test Mode (Development):**

1. Use Razorpay test keys (start with `rzp_test_`)
2. Use test UPI numbers for payment
3. All features work exactly like production

### **Production Mode:**

1. Use live Razorpay keys (start with `rzp_live_`)
2. Real payments will be processed
3. Webhooks will confirm payments automatically

## 🔹 **Payment Flow Example**

```
User Flow:
1. Enter name & mobile → Select tickets → Click "Proceed to Payment"
2. See payment page with order details
3. Click "Pay ₹X" → Razorpay window opens
4. Complete payment → Instant confirmation
5. See success message → Booking completed

Admin Flow:
1. Monitor payments in real-time
2. View all bookings in admin dashboard
3. Export data to Excel
4. Reset system for new lucky draw
```

## 🔹 **Security Features**

- ✅ **Payment signature verification**
- ✅ **Webhook signature validation**
- ✅ **Session-based user tracking**
- ✅ **Secure API key handling**
- ✅ **Input validation and sanitization**

## 🔹 **Next Steps**

1. **Get your Razorpay API keys** (most important!)
2. **Configure the keys** in `app_realtime.py`
3. **Test with test keys** first
4. **Deploy to production** with live keys
5. **Set up webhooks** for automatic confirmation

## 🔹 **Support**

If you need help:

1. Check Razorpay documentation
2. Verify API keys are correct
3. Check webhook configuration
4. Monitor server logs for errors

---

**🎉 Your Lucky Draw system now has professional real-time payment integration!**
