//반복문을 사용하여 배열 사용하기 
public class ArrayExam2 {

	public static void main(String[] args) {
		
		
		int[] iarray = new int[100];
		iarray[0] = 1;
		iarray[1] = 2;
		System.out.println(iarray.length);
		
		//iarray.length는 배열의 크기를 출력시켜줌
		for(int i = 0; i < iarray.length; i++) {
			iarray[i] = i + 1;
			}
		
		int sum = 0;	//지속적인 저장을 위해서 안에다가 선언하면 안 된다. 
		for (int i = 0; 1 < iarray.length; i++) {
			// 변수의 스코프 - 변수를 선언한 지역에 따라서 사용가능 구역이 달라진다.
			//int sum = sum + i;지속적인 저장을 위해서 안에다가 선언하면 안 된다.
			sum = sum + iarray[i];
		}
		
		System.out.println(sum);
	}

}
