FROM alpine:latest

RUN apk update

RUN apk add openjdk17 wget

WORKDIR /app

RUN wget https://bao-products-builds.s3.us-east-1.amazonaws.com/dhis2-superset-gateway/master/dhis2-superset-gateway.jar

RUN chmod +x dhis2-superset-gateway.jar

RUN addgroup --system --gid 1001 bao-admin
RUN adduser --system --uid 1001 bao-admin

RUN chown -R bao-admin:bao-admin /app

USER bao-admin

EXPOSE 8092

ENV JAVA_OPTS="-Xms512M -Xmx1024M"

CMD ["java","-jar","dhis2-superset-gateway.jar"]
