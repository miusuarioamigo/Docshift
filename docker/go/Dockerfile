FROM golang as pepe
WORKDIR /go/src/
RUN go get -d -v golang.org/x/net/html  
COPY app.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=pepe /go/src/app .
# COPY --from=nginx:latest /etc/nginx/nginx.conf /nginx.conf
CMD ["./app"]  