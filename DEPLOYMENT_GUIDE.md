# 🚀 **FREE WEBSITE DEPLOYMENT GUIDE**

## 🌐 **Best Free Hosting Options for Your Lucky Draw Website**

### **Option 1: Render (Recommended - Easiest)**

**✅ Pros:** Free tier, automatic deployments, custom domain support
**❌ Cons:** Free tier has limitations

#### **Step-by-Step Deployment on Render:**

1. **Prepare Your Code:**

   - All files are already prepared ✅
   - `Procfile` created ✅
   - `requirements.txt` updated ✅
   - `runtime.txt` created ✅

2. **Create Render Account:**

   - Go to [render.com](https://render.com)
   - Sign up with GitHub/GitLab account

3. **Deploy:**

   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app_realtime:app`
   - **Environment:** Python 3
   - Click "Create Web Service"

4. **Environment Variables (Add in Render Dashboard):**
   ```
   FLASK_ENV=production
   SECRET_KEY=your-super-secret-key-here
   ```

### **Option 2: Railway (Great Alternative)**

**✅ Pros:** Free tier, very fast, easy setup
**❌ Cons:** Limited free usage

#### **Deployment Steps:**

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Python and deploy

### **Option 3: Heroku (Classic Choice)**

**✅ Pros:** Well-established, good documentation
**❌ Cons:** No free tier anymore (paid from $5/month)

### **Option 4: PythonAnywhere (Python-Specific)**

**✅ Pros:** Python-focused, free tier available
**❌ Cons:** Limited features on free tier

## 🔧 **Pre-Deployment Checklist**

### **1. Update Configuration for Production**

- ✅ Secret key now uses environment variables
- ✅ Debug mode controlled by FLASK_ENV
- ✅ Port configuration for production

### **2. Required Files Created:**

- ✅ `Procfile` - Tells hosting platform how to run your app
- ✅ `requirements.txt` - Lists all Python dependencies
- ✅ `runtime.txt` - Specifies Python version

### **3. Environment Variables to Set:**

```
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
```

## 📁 **GitHub Repository Setup**

### **1. Create GitHub Repository:**

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it: `lucky-draw-website`
4. Make it Public (required for free hosting)
5. Don't initialize with README

### **2. Upload Your Code:**

```bash
# In your lucky_draw directory
git init
git add .
git commit -m "Initial commit - Lucky Draw Website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/lucky-draw-website.git
git push -u origin main
```

## 🚀 **Quick Deployment Steps**

### **Render (Recommended):**

1. **Upload to GitHub** (see steps above)
2. **Go to Render.com** → Sign up
3. **New Web Service** → Connect GitHub
4. **Select Repository** → lucky-draw-website
5. **Configure:**
   - Name: `lucky-draw-app`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_realtime:app`
6. **Add Environment Variables:**
   - `FLASK_ENV` = `production`
   - `SECRET_KEY` = `your-secret-key-here`
7. **Deploy!**

### **Your Website URL:**

After deployment, you'll get a URL like:
`https://lucky-draw-app.onrender.com`

## 🔧 **Post-Deployment Setup**

### **1. Update Razorpay Webhook URL:**

- Go to Razorpay Dashboard
- Settings → Webhooks
- Add webhook URL: `https://your-app-url.com/razorpay_webhook`
- Select events: `payment.captured`

### **2. Generate QR Code for Website:**

- Visit your deployed website
- Go to Admin Panel: `https://your-app-url.com/admin`
- Click "Generate QR Code"

### **3. Test the Complete Flow:**

1. Visit your website
2. Fill user details
3. Select tickets
4. Test payment (use test mode)
5. Verify admin panel works

## 💡 **Pro Tips:**

1. **Free Tier Limitations:**

   - Render: 750 hours/month free
   - Railway: $5 credit/month
   - Plan accordingly

2. **Custom Domain:**

   - Render supports custom domains
   - Point your domain to the provided URL

3. **Monitoring:**

   - Check Render/Railway dashboard for logs
   - Monitor usage to stay within free limits

4. **Backup:**
   - Your data is stored in Excel files
   - Download regularly from admin panel

## 🆘 **Troubleshooting:**

### **Common Issues:**

1. **Build Failed:** Check requirements.txt
2. **App Won't Start:** Check Procfile
3. **Database Issues:** Check file permissions
4. **Payment Issues:** Verify Razorpay keys

### **Support:**

- Render: Excellent documentation
- Railway: Active community
- GitHub: Version control and collaboration

## 🎉 **You're Ready to Deploy!**

Your Lucky Draw website is now production-ready with:

- ✅ Real-time payment integration
- ✅ Admin dashboard
- ✅ Mobile-responsive design
- ✅ QR code generation
- ✅ Excel data storage
- ✅ All deployment files prepared

**Next Step:** Choose your hosting platform and follow the deployment steps above!


