
def count_batteries_by_health(present_capacities):
  count={"healthy":0,"exchange":0,"failed":0}
  for i in present_capacities:
     soh=100*(i/120)
     if soh>80 and soh<=100:
         count["healthy"]+=1
     elif soh>62 and soh<=80:
         count["exchange"]+=1
     else:
         count["failed"]+=1
  return count
   
def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  print(counts)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
  

if __name__ == '__main__':
  test_bucketing_by_health()
