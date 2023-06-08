const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

app.use(bodyParser.urlencoded({ extended: false }));

// MongoDB와 연결합니다.
mongoose.connect('mongodb://localhost:27017/mydatabase', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

// 데이터베이스에 저장할 게시글 스키마를 정의합니다.
const postSchema = new mongoose.Schema({
  title: String,
  content: String,
  createdAt: { type: Date, default: Date.now }
});
const Post = mongoose.model('Post', postSchema);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/upload.html');
});

app.post('/upload', (req, res) => {
  const title = req.body.title;
  const content = req.body.content;

  // 폼 데이터를 사용하여 새로운 게시글을 생성합니다.
  const newPost = new Post({ title, content });

  // 게시글을 데이터베이스에 저장합니다.
  newPost.save((err) => {
    if (err) {
      console.error(err);
      res.status(500).send('게시글을 저장하는 도중에 오류가 발생했습니다.');
    } else {
      // 처리가 완료된 후 리다이렉트할 페이지로 이동
      res.redirect('/dashboard.html');
    }
  });
});

app.listen(3000, () => {
  console.log('서버가 실행 중입니다. http://localhost:3000 에서 확인할 수 있습니다.');
});
