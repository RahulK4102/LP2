import streamlit as st

st.header("Chessboard Game Expert System")

def get_info(piece):
    if piece == "Pawn":
        st.header("Pawn")
        st.write("The pawn moves forward one square, but captures diagonally. On its first move, a pawn can move two squares forward.")
        st.write("Pawns can be promoted to any other piece (queen, rook, bishop, or knight) when they reach the opponent's back rank.")
    
    elif piece == "Rook":
        st.header("Rook")
        st.write("The rook moves horizontally or vertically across the board.")
        st.write("It can move any number of squares in a straight line, but cannot jump over other pieces.")
    
    elif piece == "Knight":
        st.header("Knight")
        st.write("The knight moves in an L-shape: two squares in one direction, then one square perpendicular to that direction.")
        st.write("It is the only piece that can jump over other pieces.")
    
    elif piece == "Bishop":
        st.header("Bishop")
        st.write("The bishop moves diagonally across the board.")
        st.write("It can move any number of squares diagonally, but cannot jump over other pieces.")
    
    elif piece == "Queen":
        st.header("Queen")
        st.write("The queen combines the powers of the rook and the bishop.")
        st.write("It can move horizontally, vertically, or diagonally any number of squares, but cannot jump over other pieces.")
    
    elif piece == "King":
        st.header("King")
        st.write("The king moves one square in any direction.")
        st.write("It is the most important piece as the game ends when a player's king is in checkmate.")
    
if __name__ == "__main__":
    piece = st.selectbox(
        'Select a chess piece to learn about:',
        ("Pawn", "Rook", "Knight", "Bishop", "Queen", "King"),
        index=0,
    )

    col1, col2 = st.columns([1, 0.1])
    with col1:
        ask = st.button("Learn")
    with col2:
        quit = st.button("Quit")
    
    if ask:
        get_info(piece)
    if quit:
        st.write("Thank you for using the Chessboard Game Expert System!")
