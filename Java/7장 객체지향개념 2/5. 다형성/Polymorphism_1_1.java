package javaStandard;

class Tv{
	boolean power; //��������(on/off)
	int channel; //ä��
	
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
	String text; //ĸ�ǳ���
	void caption() {
		// ������� 
	}
}