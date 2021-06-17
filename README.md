# Toy-project

인스타그램 만들기

Django를 통해 인스타그램을 만들어보기

## 환경 설정

사용된 환경

```
asgiref==3.3.4
Django==3.2.4
pytz==2021.1
Pillow==8.2.0
sqlparse==0.4.1
```

requirements 를 이용한 패키지 설치

```
pip install -r requirements.txt
```

## 기능(상세내용은 구현 후 수정예정)

```
회원가입 - 6.4 추가 - 완료
로그인 - 6.4 추가 - 완료
사진 올리기 6.5 추가 - 진행중 > 사진 출력안됨
메인 페이지 6.7 추가 - 6.16 style 추가 - 진행중
검색 - 6.10~16 추가 - 완료
유저 상세 페이지 - 6.10~12 추가 - 진행중
사진 상세 페이지 - 6.11 추가 - 진행중
마이 페이지 - 6.12 추가 - 진행중
댓글 - 6.14 추가 - 진행중 > http 405 오류
좋아요 - 6.14~15 추가 - 완료
팔로우,팔로잉 - 6.15~16 추가 - 완료
소셜로그인 - 진행중
유저 정보 수정 - 6.15 추가 - 완료
사진 수정 - 6.16 추가 - 진행중
사진 삭제 - 진행중
```

### 문제점

```
사진 출력안됨
유저 상세 페이지에서 사진 불러오기 못함 , 사진 상세 페이지도 동일
댓글 추가 시 405 뜸
```
