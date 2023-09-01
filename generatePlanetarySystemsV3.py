import random, json, sys, itertools

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, \
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, \
    _, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'

planet_types = ['Rocky', 'Gas Giant', 'Frozen', 'Oceanic', 'Desert']
r = random.choice
planet_name = ''.join
generate_descriptor = lambda p: p  # Placeholder for descriptor generator
generate_star_system_type = lambda: ''  # Placeholder for star system type generator
generate_star_system_economy = lambda e: e  # Placeholder for star system economy generator

total_planets = 0
a_ = set()
u, t, a_ = 'designation', 'planets', 'description'

generate = lambda: [{'designation': f'{a}{b}{c}', 'classification': generate_star_system_type(),
                     'economy': generate_star_system_economy(r(1, 100)), t: [{'designation': planet_name(
                     [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
                      A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, _, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0][0]) for _ in range(5)]} for _ in range(r(3, 9))]} for a, b, c in itertools.product(
    (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
     A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, _, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0), repeat=3)]

generated_data = generate()
for solar_system in generated_data: total_planets += len(solar_system[t])
print('Total unique Solar Systems:', len(generated_data))
print('Total unique planets:', total_planets)

with open('universe.json', 'w') as json_file: json.dump(generated_data, json_file, indent=2)
