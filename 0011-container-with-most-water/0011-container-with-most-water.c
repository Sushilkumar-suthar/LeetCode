int maxArea(int* height, int heightSize) {
    int start = 0;
    int end = heightSize - 1;
    int max_area = 0;

    while (start < end) {
        int left = height[start];
        int right = height[end];
        int area = ((left < right) ? left : right) * (end - start);

        if (area > max_area)
            max_area = area;
        start += (left < right);
        end -= !(left < right);
    }
    return max_area;
}