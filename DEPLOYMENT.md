# Deployment Guide — Fashion Hub ATP

## Prerequisites

1. GitHub account
2. Render account (free tier works)
3. Cloudinary account (free tier works)

## Step-by-Step Deployment

### 1. Setup Cloudinary (Media Storage)

1. Go to https://cloudinary.com and sign up
2. After login, go to Dashboard
3. Note down these three values:
   - Cloud Name
   - API Key
   - API Secret

### 2. Push Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Fashion Hub ATP"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 3. Deploy on Render

1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select your repository
5. Render will detect `render.yaml` automatically
6. Click "Apply" to use the blueprint

### 4. Configure Environment Variables

In Render dashboard, go to your web service → Environment:

Add these variables:
- `CLOUDINARY_CLOUD_NAME` = your_cloud_name
- `CLOUDINARY_API_KEY` = your_api_key
- `CLOUDINARY_API_SECRET` = your_api_secret

Note: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `DATABASE_URL` are auto-configured by render.yaml

### 5. Wait for Build

Render will:
- Install dependencies
- Run migrations
- Seed categories automatically
- Collect static files
- Start the server

### 6. Create Admin User

After deployment succeeds:
1. Go to your service → Shell tab
2. Run this command:

```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('KVL@2005', '', '5002') if not User.objects.filter(username='KVL@2005').exists() else print('exists')"
```

### 7. Access Your Site

- Public site: `https://your-app-name.onrender.com`
- Admin panel: `https://your-app-name.onrender.com/admin`
- Login with username: `KVL@2005` and password: `5002`

## Post-Deployment

### Add Products

1. Login to admin panel
2. Click "Products" → "Add Product"
3. Fill in:
   - Name
   - Category
   - Price
   - Description (optional)
   - Upload image
4. Save

### Update Allowed Hosts

If using custom domain:
1. Go to Render dashboard → Environment
2. Update `ALLOWED_HOSTS` to include your domain
3. Save (will trigger redeploy)

## Troubleshooting

### Images not showing
- Check Cloudinary credentials are correct
- Verify images are uploaded through admin panel

### Database reset
- Render PostgreSQL is persistent
- Data survives redeployments
- Only deleted if you delete the database service

### Build fails
- Check build logs in Render dashboard
- Ensure all dependencies in requirements.txt
- Verify Python version compatibility

### Static files not loading
- Run `python manage.py collectstatic` in Shell
- Check WhiteNoise is in INSTALLED_APPS

## Maintenance

### Update Code
```bash
git add .
git commit -m "Update description"
git push
```
Render auto-deploys on push.

### Backup Database
Use Render's database backup feature or:
```bash
pg_dump DATABASE_URL > backup.sql
```

### Monitor
- Check Render logs for errors
- Monitor Cloudinary usage
- Review PostgreSQL storage

## Cost Estimate

- Render Web Service: Free tier (sleeps after inactivity)
- Render PostgreSQL: Free tier (90 days, then $7/month)
- Cloudinary: Free tier (25GB storage, 25GB bandwidth)

## Security Notes

- Never commit `.env` file
- Keep admin credentials secure
- Use strong SECRET_KEY in production
- Set DEBUG=False in production
- Regularly update dependencies

---

Need help? Contact: 7013821498
