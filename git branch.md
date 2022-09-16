## 깃 브랜치

### 조직

* 만들기
  1. +버튼의 new organization 
  2. 원하는 플랜(가격)을 정해서 진행
  3. 이름, 컨택 이메일(보통 회사 공식계정 등) 입력
  4. Next -> Complete Setup
* 구성원 초대
  1. invite someone -> 이메일 입력
* 레포 생성
  * Private 설정 안해놓으면 멤버 이외에도 접속 가능해지므로 주의

* 권한 변경
  * Member privileges -> Base permissions 값을 변경

### 브랜치 

* 만들기

  * git branch : 브랜치 리스트 표시
  * git branch '브랜치 이름' : 브랜치 생성

  * git checkout '브랜치 이름' : 브랜치 이동

    

* PR 날려주세요 = Pull Request 올려주세요
  * 한 브랜치에서 다른 한 브랜치로 내용을 합침
* conflict 났을 때는 web에서 수정하게 된다.
* 지우기
  * 웹에서 머지가 완료된 브랜치 삭제
  * 로컬 환경에서 브랜치에서 master로 체크아웃 한뒤에
    * git branch -D '브랜치 이름'
    * master pull 하기
