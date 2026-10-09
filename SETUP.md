# 🚀 GitHub Profile Setup & Customization Guide

Welcome to your redesigned, production-grade GitHub profile README! Follow this quick checklist to activate all dynamic elements, automated CI pipelines, and personalized links.

---

## 📋 Step 1: Enable GitHub Actions Workflow Permissions

Your profile includes an automated CI workflow (`snake.yml`) that generates your contribution snake animation directly into an `output` branch.

1. Go to your repository settings on GitHub:
   `https://github.com/abhipatel0000/abhipatel0000/settings/actions`
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Check **Allow GitHub Actions to create and approve pull requests** (if available).
5. Click **Save**.

---

## ⚡ Step 2: Trigger the Snake Workflow Manually

To generate the initial Snake animation immediately without waiting for the scheduled cron:

1. Go to `https://github.com/abhipatel0000/abhipatel0000/actions`.
2. Click **Generate Snake Contribution Animation** on the left menu.
3. Click **Run workflow** -> Select `main` branch -> Click green **Run workflow** button.
4. Once it finishes successfully, an `output` branch will automatically be created and your live snake contribution animation will render seamlessly on your profile!

---

## ✏️ Step 3: Personalization & TODO Placeholders Checklist

Search for `TODO` in `README.md` to update any links as you launch or publish them:

| Item | Location in `README.md` | Default Value | Your Target URL |
| :--- | :--- | :--- | :--- |
| **Portfolio Link** | Intro section quick link pill | `https://github.com/abhipatel0000` | Update to your live personal portfolio domain |
| **AURA Project** | Featured Projects (Top Left) | `https://github.com/abhipatel0000` | Update to your AURA repo or demo URL |
| **StageSync Project** | Featured Projects (Top Right) | `https://github.com/abhipatel0000` | Update to your StageSync repo or demo URL |
| **BestView Clone** | Featured Projects (Bottom Left) | `https://github.com/abhipatel0000` | Update to your BestView repo or demo URL |
| **AI Trading Bot** | Featured Projects (Bottom Right) | `https://github.com/abhipatel0000` | Update to your AI Trading Bot repo or demo URL |
| **Creative Corner** | Creative Corner card link | `https://instagram.com/abhipatel1810` | Update to your YouTube / Behance / Video Reel |

---

## 🎨 Asset Maintenance

All vector assets are self-contained SVGs located in `./assets/`.
- Every card has both dark (`*-dark.svg`) and light (`*-light.svg`) variants.
- The `generate_assets.py` script can be modified and re-run (`python generate_assets.py`) whenever you want to adjust tech stack pills, project descriptions, or brand accents.
