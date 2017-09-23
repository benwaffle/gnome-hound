Runs [Hound](https://github.com/etsy/hound) on GNOME modules.

```
$ docker build -t gnome-hound .
$ docker run -d -p 6080:6080 -v $(pwd)/db:/db gnome-hound
```

monitor indexing status with `docker logs -f <container id>`

grab a cup of coffee... wait for it to index...
when it's done, search is at http://localhost:6080
