FROM alpine:latest

RUN apk update

RUN apk add openjdk17 wget

WORKDIR /app

RUN wget https://bao-products-builds.s3.us-east-1.amazonaws.com/analytics-platform/master/bao-identity.jar

RUN chmod +x bao-identity.jar

RUN addgroup --system --gid 1001 bao-admin
RUN adduser --system --uid 1001 bao-admin

RUN chown -R bao-admin:bao-admin /app

USER bao-admin

ENV JAVA_OPTS="-Xms1024M -Xmx2048M"

EXPOSE 8086
CMD ["java", "-jar" , "bao-identity.jar"]
