def selectionSort(arr,start):
  if start < len(arr)-1: # 'start'가 배열길이보다 작은 경우에만 동작합니다. 'start'는 정렬이 완료된 배열 부분의 바로 다음 인덱스를 가리킵니다.
    minIndex = start # 가장 작은 요소의 인덱스를 추적하는 변수를 설정합니다, 초기값은 'start'로 설정합니다.
    for i in range(start+1,len(arr)): # 시작위치부터 배열의 끝까지 모든 요소를 순회합니다.
      if arr[minIndex] > arr[i]: # 만약 현재 요소가 현재 최소 요소보다 작다면,
        minIndex = i # 최소 요소의 인덱스를 현재 요소의 인덱스로 업데이트합니다.
    arr[start], arr[minIndex] = arr[minIndex], arr[start] # 시작 위치의 요소와 가장 작은 요소를 교환합니다.
    selectionSort(arr,start+1) # 배열의 다음 부분에 대해 선택 정렬을 수행합니다.

numbers=[64,34,25,12,22,11,90] # 정렬할 숫자들을 포함하는 리스트를 정의합니다.
selectionSort(numbers,0) # 정의된 리스트에 선택 정렬 함수를 적용합니다. 처음 시작 인덱스는 0입니다.
print("선택 정렬 결과 : ",numbers) # 정렬된 리스트를 출력합니다.