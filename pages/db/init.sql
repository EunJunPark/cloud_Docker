-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS mydatabases;
USE mydatabases;

-- 2. 기존 사용자 삭제 (이미 존재하는 경우)
DROP USER IF EXISTS 'admin'@'%';

-- 3. 새로운 사용자 생성 (mysql_native_password 사용)
CREATE USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'admin';

-- 4. 사용자에게 데이터베이스 접근 권한 부여
GRANT ALL PRIVILEGES ON mydatabases.* TO 'admin'@'%';

-- 5. 변경 사항 적용
FLUSH PRIVILEGES;

-- 1. 테이블 생성
CREATE TABLE IF NOT EXISTS board (
    idx INT AUTO_INCREMENT PRIMARY KEY,   
    name VARCHAR(100) NOT NULL,          
    pw VARCHAR(255) NOT NULL,             
    context TEXT NOT NULL,                
    currentstatus TINYINT DEFAULT 1       
);

