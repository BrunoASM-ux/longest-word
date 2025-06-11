from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        game = Game()
        grid = game.grid

        # Verifica que sea una lista
        assert isinstance(grid, list)
        # Verifica que tenga 9 letras
        assert len(grid) == 9
        # Verifica que todas sean letras mayúsculas
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        new_game.grid = list(test_grid)
        assert new_game.is_valid(test_word) is True
        assert new_game.grid == list(test_grid)

    def test_is_invalid(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        new_game.grid = list(test_grid)
        assert new_game.is_valid(test_word) is False
        assert new_game.grid == list(test_grid)
