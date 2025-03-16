# Cloud Docker Project

# flask:80/ mysql: 3307
이 프로젝트는 **Docker**와 **Flask**를 이용한 **MySQL 연동 웹 애플리케이션**입니다. 
이 문서는 **Windows**와 **Linux**에서 Docker를 설정하고 애플리케이션을 실행하는 방법을 안내합니다.

## 시작하기
### **Docker가 실행 중이여야합니다.**

### **1. Git 저장소 클론**

먼저, Git 저장소를 클론합니다. 터미널 또는 명령 프롬프트에서 아래 명령어를 입력하여 저장소를 클론하세요.

#### Windows (CMD 관리자 권한): Linux (su 권한)
git clone https://github.com/EunJunPark/cloud_Docker.git

#### 2. 디렉토리로 이동
저장소를 클론한 후, 해당 디렉토리로 이동합니다. cd 명령어를 사용하여 디렉토리로 이동하세요.

cd cloud_Docker

#### 3. Docker Compose로 애플리케이션 실행
애플리케이션을 실행하기 위해 Docker Compose를 사용합니다. docker-compose.yml 파일이 포함되어 있어, Docker와 MySQL 컨테이너를 한 번에 빌드하고 실행할 수 있습니다.

아래 명령어를 실행하여 애플리케이션을 빌드하고 시작합니다:

docker-compose up --build
이 명령어는 Docker Compose가 정의한 서비스들을 빌드하고 시작합니다. 애플리케이션을 처음 실행할 때는 빌드 시간이 조금 걸릴 수 있습니다.

4. 웹 애플리케이션 접속
애플리케이션이 실행된 후, 웹 브라우저에서 아래 주소로 접속합니다.

http://localhost
브라우저에서 localhost 주소로 접속하면, Flask 애플리케이션이 실행되는 웹 페이지를 볼 수 있습니다.

