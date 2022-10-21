# DB 테이블 추가하기

```sql


CREATE TABLE trfacd_status (
	trfacd_type varchar(30) comment '교통사고 종류' PRIMARY KEY,
	injury int(4) COMMENT '부상',
	dead int(4) COMMENT '사망'
);


-- 지역구 정보 테이블
CREATE TABLE area (
	anum varchar(30) comment '지역 번호' PRIMARY KEY,
	aname varchar(30) comment '구 이름'
	);

-- 교통사고 관리 정보 테이블
CREATE TABLE trfacd_info(
	 trfacd_mngno varchar(30) comment '사고 관리 번호' PRIMARY KEY,
	 trfacd_date datetime comment '교통사고 날짜',
	 trfacd_type varchar(30) comment '교통사고 종류',
	 FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE,
	 trfacd_loc varchar(30) comment '교통사고 발생지'
);

-- 지역별 교통사고 정보 테이블
CREATE TABLE area_trfacd (
	atnum varchar(30) comment '지역 사고 번호' PRIMARY KEY,
	anum varchar(30) comment '지역 번호',
	dong_name varchar(30) comment ' 동 이름',
	cctv varchar(30) comment '사고지역 CCTV 여부',
	scamera varchar(30) comment '사고지역 과속카메라 여부',
	sbrtyCheck varchar(30) comment '사고지역 음주단속 여부',
	trfacd_mngno varchar(30) comment '사고 관리 번호',
	FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE
	);

-- 교통사고 당사자 테이블
CREATE TABLE trfacd_prt (
prt_mngno varchar(30) comment '당사자 관리 번호' PRIMARY KEY,
pname varchar(30) comment '이름',
psex varchar(30) comment '성별',
pbrth varchar(30) comment '생년월일',
pdrivSLic varchar(30) comment '면허유무',
psBelt varchar(30) comment '안전벨트 유무',
pcasualty varchar(30) comment '부상/사망 유무',
pdriking varchar(30) comment '음주 여부',
pspeed int(4) comment '사고직전 속도',
trfacd_mngno varchar(30) comment '사고 관리 번호',
FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE,
trfacd_type varchar(30) comment '교통사고 종류',
FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE
)

```

```sql
CREATE TABLE trfacd_status (
	trfacd_type varchar(30) comment '교통사고 종류' PRIMARY KEY,
	injury int(4) COMMENT '부상',
	dead int(4) COMMENT '사망'
);

DROP TABLE trfacd_status

CREATE TABLE area (
	anum varchar(30) comment '지역 구 번호' PRIMARY KEY,
	aname varchar(30) comment '구 이름'
	);


CREATE TABLE trfacd_info(
	 trfacd_mngno varchar(30) comment '사고 관리 번호' PRIMARY KEY,
	 trfacd_date datetime comment '교통사고 날짜',
	 trfacd_loc varchar(30) comment '교통사고 발생지',
	 trfacd_type varchar(30) comment '교통사고 종류',
	 FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE
);

CREATE TABLE area_trfacd (
	atnum varchar(30) comment '지역 사고 번호' PRIMARY KEY,
	anum varchar(30) comment '지역 구 번호',
	FOREIGN KEY (anum) REFERENCES area(anum) ON DELETE CASCADE,
	dong_name varchar(30) comment ' 사고지역 동 이름',
	atmiddle varchar(30) comment '사고지역 중앙 분리대',
	atscamera varchar(30) comment '사고지역 과속카메라',
	atsvcamera varchar(30) comment '사고지역 신호위반 카메라',
	atbrtyCheck varchar(30) comment '사고지역 음주 단속',
	trfacd_mngno varchar(30) comment '사고 관리 번호',
	FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE
	);

DROP TABLE trfacd_status, trfacd_info, area
DROP TABLE area_trfacd


CREATE TABLE trfacd_prt (
pno varchar(30) comment '당사자 번호' PRIMARY KEY,
pname varchar(30) comment '당사자 이름',
psex varchar(30) comment '당사자 성별',
pbrth varchar(30) comment '당사자 생년월일',
pdriverl varchar(30) comment '당사자 면허 유무',
psBelt varchar(30) comment '당사자 안전벨트 유무',
pdriking varchar(30) comment '당사자 음주 여부',
pcasualty varchar(30) comment '당사자 부상/사망 유무',
trfacd_type varchar(30) comment '교통사고 종류',
FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE,
trfacd_date datetime comment '교통사고 날짜',
trfacd_speed int(4) comment '교통사고 직전 속도',
trfacd_mngno varchar(30) comment '사고 관리 번호',
FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE
)

```