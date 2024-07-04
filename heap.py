import heapq

heap=[] # 힙으로 이용할 리스트 생성

heapq.heappush(heap,5)
print(heap)
heapq.heappush(heap,3)
print(heap)
heapq.heappush(heap,7)
print(heap)
heapq.heappush(heap,1) # [3,5,7,1] > [1,5,7,3] > [1,3,7,5] > [1,3,5,7]
print(heap) # print는 [1,3,7,5]로 나오지만 외부에서는 [1,3,5,7]로 정렬 되어있다.

# 꺼내기 : 힙의 가장 작은 요소를 제거하고 반환합니다.
small=heapq.heappop(heap)
print("small로 꺼낸 값 : ",small)
print("small이 나간 뒤 heap 값 : ",heap)
# small=1
# heap=[3,5,7]

small_next=heapq.heappop(heap)
print("small_next로 꺼낸 값 : ",small_next)
print("small_next가 나간 뒤 heap 값 : ",heap)
# small_next=3
# heap=[5,7]

# 가장 작은 요소 n개 꺼내기
heap2 = [1,3,5,7,9,10,11,20]

smallHeap = heapq.nsmallest(3,heap2) # heap2에서 앞의 3개를 가져옴
print("heap2의 현재 값 : ",heap2)
print("heap2에서 가장 작은 값 3개 : ",smallHeap) # 위의 heappop과는 다르게 값을 제거하지 않음

# 가장 큰 요소 n개 꺼내오기
largeHeap = heapq.nlargest(3,heap2)
print("heap2의 현재 값 : ",heap2)
print("heap2에서 가장 큰 값 3개 : ",largeHeap)

print(heap2[2])