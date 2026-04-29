class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        return self.dfs(image,sr,sc,origin,color)
        
    def dfs(self, image, sr,sc,origin, color):
        ROWS, COLS = len(image), len(image[0])

        if min(sr,sc) < 0 or sr == ROWS or sc == COLS or image[sr][sc] == color or image[sr][sc]!=origin:
            return image

        if image[sr][sc] == origin:
            image[sr][sc] = color

        self.dfs(image,sr+1,sc,origin,color)
        self.dfs(image,sr,sc+1,origin,color)
        self.dfs(image,sr-1,sc,origin,color)
        self.dfs(image,sr,sc-1,origin,color)

        return image




