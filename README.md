# 🎯 Lucky Draw Website

A modern, mobile-responsive web application for managing lucky draw ticket bookings with real-time payment integration.

## ✨ Features

- 🎫 **Ticket Selection**: Interactive ticket grid with animations
- 💳 **Manual Payments**: UPI integration with transaction verification
- 📱 **Mobile-Responsive**: Works perfectly on all devices
- 🔧 **Admin Dashboard**: Complete management interface
- 📊 **Data Management**: Excel-based data storage and export
- 🎨 **Modern UI**: Beautiful design with TailwindCSS
- 🔔 **Real-time Updates**: WebSocket integration for live updates
- 📱 **QR Code Generation**: Easy access via QR codes

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/lucky-draw-website.git
cd lucky-draw-website

# Install dependencies
pip install -r requirements.txt

# Run the application
python app_realtime.py
```

### Access URLs

- **Website**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin

## 🛠️ Technology Stack

- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript, TailwindCSS
- **Payment**: UPI Integration with Manual Verification
- **Database**: Excel (pandas)
- **Real-time**: WebSocket (Socket.IO)

## 📁 Project Structure

```
lucky-draw/
├── app_realtime.py          # Main Flask application
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
├── data/                    # Excel files and data
├── requirements.txt         # Python dependencies
├── Procfile                 # Deployment configuration
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables

```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### UPI Setup

1. Configure your UPI ID in `app_realtime.py`
2. Set up QR code for easy payment scanning
3. Train admin users on payment verification process

## 🚀 Deployment

This application is ready for deployment on:

- **Render** (Recommended)
- **Railway**
- **Heroku**
- **PythonAnywhere**

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

## 📊 Admin Features

- View all bookings
- Export data to Excel
- Reset data for new draws
- Monitor payments
- Generate QR codes
- Manage ticket availability

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

- Check the deployment guide
- Review the admin documentation
- Contact the development team

---

**Built with ❤️ for seamless lucky draw management**
