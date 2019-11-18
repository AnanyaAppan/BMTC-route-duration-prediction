length_lat = 0.032/2
length_long = 0.043/2

lat = 12.66 
long = 77.27 
# Assuming the origin is (lat, long), coming up with grid number

def get_grid(lat_test, long_test):
    grid_i = int(((lat_test-lat)/length_lat))
    grid_j = int(((long_test-long)/length_long))
    grid_num = grid_i * 34 + grid_j
    grid_lat = 12.66 + grid_i*(length_lat)
    grid_long = 77.27 + grid_j*(length_long)
    grid_length_lat = length_lat/10
    grid_length_long = length_long/10
    subgrid_i = int(((lat_test-grid_lat)/grid_length_lat))
    subgrid_j = int(((long_test-grid_long)/grid_length_long))
    subgrid_num = subgrid_i*10 + subgrid_j
    return grid_num, subgrid_num