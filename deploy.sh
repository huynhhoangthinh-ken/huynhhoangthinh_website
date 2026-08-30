#!/bin/bash
# ==========================================================
# Automated One-Click Deployment for huynhhoangthinh.com
# Synchronizes both GitHub Repository and Cloudflare Pages
# ==========================================================

set -e

echo "🚀 [1/3] Checking and staging changes..."
git status

COMMIT_MSG="${1:-Update website content and assets}"

if [[ -n $(git status -s) ]]; then
  echo "📦 [2/3] Committing & pushing to GitHub origin main..."
  git add -A
  git commit -m "$COMMIT_MSG"
  git push origin main
else
  echo "ℹ️ No uncommitted Git changes detected."
fi

echo "⛅ [3/3] Deploying directly to Cloudflare Pages (huynhhoangthinh.com)..."
npx -y wrangler pages deploy . --project-name=huynhhoangthinh --commit-dirty=true

echo "✅ Deployment completed successfully!"
echo "🌐 Verifying live site: https://huynhhoangthinh.com"
curl -s -I https://huynhhoangthinh.com | head -n 5
