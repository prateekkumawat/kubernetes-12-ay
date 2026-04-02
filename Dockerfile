# create base source images
FROM nginx:latest

# copy content 
COPY src/ /usr/share/nginx/html 

EXPOSE 80/tcp


