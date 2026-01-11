import astropy.units as u
from dust_extinction.parameter_averages import G23
from dust_extinction.averages import G03_SMCBar


def main():
    print('=' * 50)
    print('🌌  Pixi Astronomy Demo: Conda + PyPI')
    print('=' * 50)

    # Define H-alpha wavelength
    h_alpha = 6563 * u.Angstrom
    print(f'Target Line: H-alpha ({h_alpha})')

    # Initialize Extinction Models
    # 1. Milky Way (Gordon et al. 2023) - Using defaults
    mw_model = G23(Rv=3.1)

    # 2. SMC Bar (Gordon et al. 2003) - PyPI package functionality
    smc_model = G03_SMCBar()

    # Calculate Extinction
    # We want A(lambda) / A(V)
    ext_mw = mw_model(h_alpha)
    ext_smc = smc_model(h_alpha)

    print('--- Extinction Results A(lambda) / A(V) ---')
    print(f'Milky Way (Rv=3.1):  {ext_mw:.4f}')
    print(f'SMC Bar (Gordon03):  {ext_smc:.4f}')


if __name__ == '__main__':
    main()
