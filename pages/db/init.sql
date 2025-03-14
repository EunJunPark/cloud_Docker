CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- 1. 테이블 생성
CREATE TABLE IF NOT EXISTS board (
    idx INT AUTO_INCREMENT PRIMARY KEY,   
    name VARCHAR(100) NOT NULL,          
    pw VARCHAR(255) NOT NULL,             
    context TEXT NOT NULL,                
    currentstatus TINYINT DEFAULT 1       
);


-- 3. 기존 사용자 삭제 (이미 존재하는 경우)
DROP USER IF EXISTS 'myuser'@'%';

-- 4. 새로운 사용자 생성
CREATE USER 'myuser'@'%' IDENTIFIED BY '1234';

-- 5. 사용자에게 데이터베이스 접근 권한 부여
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%';

-- 6. 변경 사항 적용
FLUSH PRIVILEGES;
