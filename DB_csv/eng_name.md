# 교통사고 예방 시스템 시스템 용어 정의

## 용어 정의

- 교통사고 발생 현황 : trfacd_status

      교통사고 종류 : trfacd_type
      부상 : injury
      사망 : dead

- 교통사고 정보 (테이블 이름) : trfacd_info
      
      사고 관리 번호 : trfacd_mngno
      교통사고 날짜 :  trfacd_date
      교통사고 발생지 : trfacd_loc
      교통사고 종류 : trfacd_type

- 교통사고 당사자 (테이블 이름) : trfacd_prt

      당사자 번호 : pno
      당사자 성별 : pname
      당사자 생년월일 : pbrth
      당사자 면허 유무 : pdriverl
      당사자 안전벨트 유무 : pbelt
      당사자 음주 유무 : pdriking
      당사자 부상/사망 여부 : pcasualty
      교통사고 종류 : trfacd_type
      교통사고 날짜 : trfacd_date
      교통사고 직전 속도 : trfacd_speed
      교통사고 발생지 : trfacd_loc
      교통사고 관리 번호 : trfacd_mngno
      

- 지역 구 테이블(테이블 이름) : area

      지역 구 번호 : anum
      구 이름 :	aname

- 지역 구별 교통사고 (테이블 이름) : area_trfacd

      지역 사고 번호 : atnum
      지역 구 번호 : anum
      사고지역 동 이름 : dong_name
      사고지역 중앙 분리대 : atmiddle
      사고지역 과속카메라 여부 : atscamera
      사고지역 신호위반 카메라 : atsvcamera
      사고지역 음주 단속 여부 : atbrtyCheck
      사고 관리 번호 : trfacd_mngno

