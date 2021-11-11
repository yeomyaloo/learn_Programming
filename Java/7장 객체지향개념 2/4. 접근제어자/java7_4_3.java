package javaStandard;

final class FinalTest{
	
	final int MAX_SIZE = 10; //멤버 변수
	
	final void getMaxSize() {
		final int LV = MAX_SIZE; // 지역변수 ---> 메소드 안에 있으니까
		return MAX_SIZE;
	}	
}

clsaa Child extends FinalTest{
	void getMaxSize() {} // 에러, 오버라이딩 불가
}