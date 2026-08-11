const fs = require('fs');
const path = require('path');

const file = '/Users/kenhuynh/Desktop/huynh-hoang-thinh-website/data/posts.json';
let posts = JSON.parse(fs.readFileSync(file, 'utf8'));

const batchFile = process.argv[2];
if (!batchFile) {
  console.error("Please provide a batch file to process");
  process.exit(1);
}

const batchData = JSON.parse(fs.readFileSync(path.resolve(batchFile), 'utf8'));

batchData.forEach(newPost => {
  const index = posts.findIndex(p => p.id === newPost.id);
  if (index !== -1) {
    posts[index].image = newPost.image;
    posts[index].excerpt = newPost.excerpt;
    posts[index].content = newPost.content;
  }
});

fs.writeFileSync(file, JSON.stringify(posts, null, 2));
console.log(`Successfully applied ${batchFile}`);
