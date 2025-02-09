import pytest
from piece import Piece

def test_piece_is_pawn():

    assert Piece.BLACK_PAWN.is_pawn()
    assert Piece.WHITE_PAWN.is_pawn()
    assert not Piece.BLACK_ROOK.is_pawn()
    assert not Piece.BLACK_KNIGHT.is_pawn()
    assert not Piece.BLACK_BISHOP.is_pawn()
    assert not Piece.BLACK_QUEEN.is_pawn()
    assert not Piece.BLACK_KING.is_pawn()

def test_piece_is_rook():
    assert Piece.BLACK_ROOK.is_rook()
    assert Piece.WHITE_ROOK.is_rook()
    assert not Piece.BLACK_PAWN.is_rook()
    assert not Piece.BLACK_KNIGHT.is_rook()
    assert not Piece.BLACK_BISHOP.is_rook()
    assert not Piece.BLACK_QUEEN.is_rook()
    assert not Piece.BLACK_KING.is_rook()

def test_piece_is_knight():
    assert Piece.BLACK_KNIGHT.is_knight()
    assert Piece.WHITE_KNIGHT.is_knight()
    assert not Piece.BLACK_PAWN.is_knight()
    assert not Piece.BLACK_ROOK.is_knight()
    assert not Piece.BLACK_BISHOP.is_knight()
    assert not Piece.BLACK_QUEEN.is_knight()
    assert not Piece.BLACK_KING.is_knight()

def test_piece_is_bishop():
    assert Piece.BLACK_BISHOP.is_bishop()
    assert Piece.WHITE_BISHOP.is_bishop()
    assert not Piece.BLACK_PAWN.is_bishop()
    assert not Piece.BLACK_ROOK.is_bishop()
    assert not Piece.BLACK_KNIGHT.is_bishop()
    assert not Piece.BLACK_QUEEN.is_bishop()
    assert not Piece.BLACK_KING.is_bishop()

def test_piece_is_queen():
    assert Piece.BLACK_QUEEN.is_queen()
    assert Piece.WHITE_QUEEN.is_queen()
    assert not Piece.BLACK_PAWN.is_queen()
    assert not Piece.BLACK_ROOK.is_queen()
    assert not Piece.BLACK_KNIGHT.is_queen()
    assert not Piece.BLACK_BISHOP.is_queen()
    assert not Piece.BLACK_KING.is_queen()

def test_piece_is_king():
    assert Piece.BLACK_KING.is_king()
    assert Piece.WHITE_KING.is_king()
    assert not Piece.BLACK_PAWN.is_king()
    assert not Piece.BLACK_ROOK.is_king()
    assert not Piece.BLACK_KNIGHT.is_king()
    assert not Piece.BLACK_BISHOP.is_king()
    assert not Piece.BLACK_QUEEN.is_king()

