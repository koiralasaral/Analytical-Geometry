# ----------------------- Parametric Curve Example: Cycloid -----------------------
# Define the parameter
t = sp.symbols('t', real=True)
x_expr = t - sp.sin(t)
y_expr = 1 - sp.cos(t)

# First and second derivatives for x(t) and y(t)
xprime_expr = sp.diff(x_expr, t)
xprime2_expr = sp.diff(x_expr, t, 2)
yprime_expr = sp.diff(y_expr, t)
yprime2_expr = sp.diff(y_expr, t, 2)

# Define the curvature for a parametric curve:
# κ(t) = |x'(t) * y″(t) - y'(t) * x″(t)| / ( (x'(t)^2 + y'(t)^2)^(3/2) )
curvature_param_expr = sp.Abs(xprime_expr * yprime2_expr - yprime_expr * xprime2_expr) / ( (xprime_expr**2 + yprime_expr**2)**(sp.Rational(3, 2)) )
radius_param_expr = 1 / curvature_param_expr

print("\nParametric Cycloid:")
print("x(t) =", x_expr)
print("y(t) =", y_expr)
print("Curvature κ(t) =", sp.simplify(curvature_param_expr))
print("Radius of Curvature R(t) =", sp.simplify(radius_param_expr))

# Lambdify the expressions for numeric evaluation
x_func = sp.lambdify(t, x_expr, 'numpy')
y_func = sp.lambdify(t, y_expr, 'numpy')
curvature_param = sp.lambdify(t, curvature_param_expr, 'numpy')
radius_param = sp.lambdify(t, radius_param_expr, 'numpy')

# Create a range of parameter values.
t_vals = np.linspace(0, 4 * np.pi, 400)
x_vals_param = x_func(t_vals)
y_vals_param = y_func(t_vals)
k_vals_param = curvature_param(t_vals)
R_vals_param = radius_param(t_vals)

# Plot the cycloid
plt.figure(figsize=(10, 6))
plt.plot(x_vals_param, y_vals_param, label='Cycloid: x=t-sin(t), y=1-cos(t)')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Cycloid Curve')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Plot curvature and radius for the cycloid
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel('t')
ax1.set_ylabel('Curvature κ(t)', color='tab:red')
ax1.plot(t_vals, k_vals_param, color='tab:red', label='Curvature κ(t)')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.set_ylabel('Radius of Curvature R(t)', color='tab:blue')
ax2.plot(t_vals, R_vals_param, color='tab:blue', label='Radius of Curvature R(t)')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.legend(loc='upper right')

plt.title('Curvature and Radius of Curvature for the Cycloid')
plt.grid(True)
plt.show()
