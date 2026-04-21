app.get('/user', (req, res) => {
    // Directly trusting query parameters can lead to NoSQL injection
    db.collection('users').findOne({ username: req.query.username }, (err, user) => {
        if (err) throw err;
        res.json(user);
    });
});

#fix
const username = String(req.query.username);

db.collection('users').findOne(
    { username: username },
    (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    }
);