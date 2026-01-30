---
description: Deploy the portfolio to GitHub Pages
---

# Deploy to GitHub Pages

Follow these steps to deploy your portfolio to the internet.

// turbo
1. **Commit and Push changes**
   Run the following command to push all local changes to GitHub:
   ```powershell
   git add .
   git commit -m "Complete portfolio stories and disclaimer"
   git push origin main
   ```

2. **Enable GitHub Pages on GitHub**
   - Go to your repository on GitHub: [noguchi-portfolio](https://github.com/sasoli0502/noguchi-portfolio)
   - Click on **Settings** (top tab).
   - In the left sidebar, click on **Pages**.
   - Under **Build and deployment** > **Source**, ensure it is set to "Deploy from a branch".
   - Under **Branch**, select `main` and `/ (root)`.
   - Click **Save**.

3. **View your site**
   - It may take a minute or two to build.
   - Your site will be available at: `https://sasoli0502.github.io/noguchi-portfolio/profile.html`
