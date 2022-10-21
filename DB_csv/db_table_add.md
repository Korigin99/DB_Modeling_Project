# DB 테이블 추가하기

```sql


CREATE TABLE trfacd_status(
	trfacd_type varchar(30) comment '교통사고 종류' PRIMARY KEY,
	injury int(4) comment '부상',
	dead int(4) comment '사망'
);

CREATE TABLE trfacd_info(
	trfacd_mngno varchar(30) comment '사고 관리 번호' PRIMARY KEY,
	trfacd_date datetime comment '교통사고 날짜',
	trfacd_loc varchar(30) comment '교통사고 발생지',
	trfacd_type varchar(30) comment '교통사고 종류',
	FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE
);

CREATE TABLE trfacd_prt(
	pno varchar(30) comment '당사자 번호' PRIMARY KEY,
	pname varchar(30) comment '당사자 이름',
	psex varchar(30) comment '당사자 성별',
	pbrth datetime comment '당사자 생년월일',
	pdriverl varchar(30) comment '당사자 운전면허 유무',
	pbelt varchar(30) comment '당사자 안전벨트 유무',
	pdriking varchar(30) comment '당사자 음주 유무',
	pcasualty varchar(30) comment '당사자 부상/사망 여부',
	trfacd_type varchar(30) comment '교통사고 종류',
	FOREIGN KEY (trfacd_type) REFERENCES trfacd_status(trfacd_type) ON DELETE CASCADE,
	trfacd_date datetime comment '교통사고 날짜',
	trfacd_speed int(4) comment '교통사고 직전 속도',
	trfacd_mngno varchar(30) comment '사고 관리 번호',
	FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE
	);


	CREATE TABLE area(
		anum varchar(30) comment '지역 구 번호' PRIMARY KEY,
		aname varchar(30) comment '지역 구 이름'
	);
	
	CREATE TABLE area_trfacd(
		atnum varchar(30) comment '지역 사고 번호' PRIMARY KEY,
		anum varchar(30) comment '지역 구 번호',
		FOREIGN KEY (anum) REFERENCES area(anum) ON DELETE CASCADE,
		dong_name varchar(30) comment '사고지역 동 이름',
		atmiddle varchar(30) comment '사고지역 중앙 분리대',
		atscamera varchar(30) comment '사고지역 과속카메라 여부',
		atsvcamera varchar(30) comment '사고지역 신호위반 카메라',
		atbrtyCheck varchar(30) comment '사고지역 음주 단속 여부',
		trfacd_mngno varchar(30) comment '사고 관리 번호',
		FOREIGN KEY (trfacd_mngno) REFERENCES trfacd_info(trfacd_mngno) ON DELETE CASCADE
	);

```