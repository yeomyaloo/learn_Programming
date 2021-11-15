package javaStandard;

class Tv{
	boolean power; //전원상태(on/off)
	int channel; //채널
	
	void power() {
		power = !power;
	}
	void channelUp() {
		++channel;
	}
	void channelUDown() {
		--channel;
	}
}

class CaptionTv extends Tv{
	String text; //캡션내용
	void caption() {
		// 내용생략 
	}
}