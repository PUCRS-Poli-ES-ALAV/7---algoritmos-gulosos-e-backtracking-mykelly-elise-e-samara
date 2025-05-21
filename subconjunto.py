import time
import pandas as pd

class SubsetSumBacktracking:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.iterations_one = 0
        self.iterations_all = 0
    
    def find_one_subset(self):
        self.iterations_one = 0
        result = []
        found = self._backtrack_one(0, [], 0, result)
        if found:
            return result, self.iterations_one
        else:
            return None, self.iterations_one
    
    def _backtrack_one(self, index, current, current_sum, result):
        self.iterations_one += 1
        # Se soma zero e não vazio, achou solução
        if current_sum == 0 and len(current) > 0:
            result.extend(current)
            return True
        if index == self.n:
            return False
        
        # Escolhe incluir nums[index]
        if self._backtrack_one(index+1, current + [self.nums[index]], current_sum + self.nums[index], result):
            return True
        # Escolhe não incluir nums[index]
        if self._backtrack_one(index+1, current, current_sum, result):
            return True
        
        return False

    def find_all_subsets(self):
        self.iterations_all = 0
        results = []
        self._backtrack_all(0, [], 0, results)
        return results, self.iterations_all
    
    def _backtrack_all(self, index, current, current_sum, results):
        self.iterations_all += 1
        if index == self.n:
            if current_sum == 0 and len(current) > 0:
                results.append(current[:])  # copia da lista
            return
        
        # Escolhe incluir nums[index]
        self._backtrack_all(index+1, current + [self.nums[index]], current_sum + self.nums[index], results)
        # Escolhe não incluir nums[index]
        self._backtrack_all(index+1, current, current_sum, results)

def test_case_bt(nums):
    print(f"Testando conjunto: {nums}\n")
    solver = SubsetSumBacktracking(nums)
    
    start = time.time()
    sol, iter_one = solver.find_one_subset()
    end = time.time()
    time_one = end - start
    
    start = time.time()
    sols_all, iter_all = solver.find_all_subsets()
    end = time.time()
    time_all = end - start
    
    # Mostrar tabela só com números e contagens
    data = {
        "Método": ["Primeira solução", "Todas soluções"],
        "Iterações": [iter_one, iter_all],
        "Tempo (s)": [time_one, time_all],
        "Número de soluções": [1 if sol else 0, len(sols_all)]
    }
    df = pd.DataFrame(data)
    
    print(df)
    print()
    
    # Mostrar as soluções completas explicitamente
    print("Primeira solução encontrada:")
    print(sol)
    print("\nTodas as soluções encontradas:")
    for i, subset in enumerate(sols_all, 1):
        print(f"{i}: {subset}")
    
    print("\n---\n")
    return df


# Exemplos de teste
dfs_bt = []
dfs_bt.append(test_case_bt([-7, -3, -2, 5, 8]))         
dfs_bt.append(test_case_bt([1, 2, 3, 4, 5, -10]))       
dfs_bt.append(test_case_bt([1, 2, 3]))                  
dfs_bt.append(test_case_bt([0, 0, 0]))                  
